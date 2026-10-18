# Examples

Concrete patterns for selected checklist items. Look up by slug ID and load this file only when needed.

## `core/names-reveal-intent`

```python
# bad
number_of_widgets = True
name = "yellow"


def turn_green():
    return "yellow"


# good
has_widgets = True
favorite_color = "yellow"


def make_yellow():
    return "yellow"
```

## `core/check-every-return`

```go
// bad
data, _ := os.ReadFile(path)
return parseConfig(data)

// good
data, err := os.ReadFile(path)
if err != nil {
    return Config{}, fmt.Errorf("read config %q: %w", path, err)
}
return parseConfig(data)
```

## `core/no-swallowed-exceptions`

```python
# bad
try:
    save(record)
except Exception:
    pass

# good
try:
    save(record)
except DiskFull:
    rotate_logs()
    save(record)
```

## `core/root-cause`

```python
# bad: clamps the symptom
def total(items):
    value = sum(item.price for item in items)
    return max(value, 0)


# good: rejects the invalid source state
def total(items):
    for item in items:
        if item.price < 0:
            raise InvalidPrice(item)
    return sum(item.price for item in items)
```

## `core/no-implementation-mirror`

```ts
// bad: verifies implementation trivia
it("calls normalizeEmail twice", () => {
  expect(normalizeEmail).toHaveBeenCalledTimes(2);
});

// good: verifies behavior
it("deduplicates users with case-insensitive emails", () => {
  const users = dedupeUsers([
    { email: "Ava@example.com" },
    { email: "ava@example.com" },
  ]);
  expect(users).toHaveLength(1);
});
```

## `simplification/dry-with-care`

```python
# bad: premature shared abstraction for cases that will diverge
def format_doc(doc):
    return f"{doc.id}: {doc.total:.2f}"


# good: keep distinct behavior distinct
def format_invoice(invoice):
    return f"INV {invoice.id}: {invoice.total:.2f} (net 30)"


def format_receipt(receipt):
    return f"RCPT {receipt.id}: paid {receipt.total:.2f}"
```

## `errors/graceful-shutdown`

```python
# bad: worker can outlive the resource it uses
def serve():
    pool = ConnectionPool()
    Thread(target=worker, args=(pool,)).start()
    run_until_signal()
    pool.close()


# good: cancellation and join order are explicit
def serve():
    pool = ConnectionPool()
    stop = threading.Event()
    thread = Thread(target=worker, args=(pool, stop))
    thread.start()
    try:
        run_until_signal()
    finally:
        stop.set()
        thread.join(timeout=5)
        pool.close()
```

## `errors/no-implicit-assumptions`

```python
# bad
qty = order["quantity"]
total = price * qty

# good
if "quantity" not in order:
    raise BadOrder("missing quantity")
qty = order["quantity"]
assert qty > 0, "quantity must be positive"
total = price * qty
```

## `bugs/one-hypothesis`

```text
bad:
  Change parsing, add retries, increase timeout, and update fixtures.

good:
  Hypothesis: parser drops events when timestamp has no timezone.
  Check: add one fixture with a timezone-free timestamp and run parser tests.
  Next: change parser behavior only if that test reproduces the failure.
```

## `bugs/bisect-history`

```text
Bug: parser fails on a large input.

1. Test the first half and second half.
2. Keep the failing half.
3. Repeat until the offending input is isolated.

The same shape works for commits, config flags, and dependency versions.
```

## `design/loose-coupling`

```python
# bad: Order and Invoice depend on each other
class Order:
    def invoice(self):
        return Invoice(self)


class Invoice:
    def __init__(self, order):
        self.order = order


# good: Invoice depends on a small capability
class Priced(Protocol):
    def total(self) -> float: ...


class Invoice:
    def __init__(self, source: Priced):
        self.source = source
```

## `design/api-prevents-misuse`

```python
# bad: caller can forget cleanup
file = open_file(path)
read(file)

# good: correct cleanup is part of the call shape
with open_file(path) as file:
    read(file)
```

## `git/atomic-commits`

```text
bad:
  fix stuff

good:
  Reject negative quantities in order parser

  Validate at the parser boundary so every caller gets a uniform
  error instead of a silent miscalculation.
```

## `release/clean-checkout`

```text
bad:
  Build from a working tree with untracked files and unknown edits.

good:
  Check out the release version in a clean directory, install from
  lockfiles, run the release command, and record the artifact identity.
```
