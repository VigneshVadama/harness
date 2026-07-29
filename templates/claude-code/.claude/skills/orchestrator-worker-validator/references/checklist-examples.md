# Examples

Concrete patterns for selected checklist items. Look up by slug ID and load this file only when needed.

## `naming/reveal-intent`

```python
# bad
def conv(d):
    return d * 86400

# good
SECONDS_PER_DAY = 86_400

def days_to_seconds(days):
    return days * SECONDS_PER_DAY
```

## `naming/no-lies`

```python
# bad
number_of_widgets = True
name = "yellow"
def turn_green(): return "yellow"

# good
has_widgets = True
favorite_color = "yellow"
def make_yellow(): return "yellow"
```

## `naming/exploit-context`

```python
# bad
class WidgetList:
    def number_of_widgets(self) -> int: ...
    def add_widget(self, widget: Widget): ...

# good
class WidgetList:
    def size(self) -> int: ...
    def add(self, widget: Widget): ...
```

## `presentation/layout-prevents-bugs`

```c
// bad: misleading indentation; exit always runs
if (!ok)
    log_error();
    exit(1);

// good: control flow is unambiguous
if (!ok) {
    log_error();
    exit(1);
}
```

## `presentation/structure-as-prose`

```python
# bad: one wall of unrelated steps
def handle_order(order):
    order = sanitize(order)
    if not order.is_valid:
        raise InvalidOrder
    inventory.reserve(order.items)
    payments.charge(order.customer, order.total)
    notifications.send(order.customer, "confirmed")
    audit.record(order)

# good: visual paragraphs follow the work
def handle_order(order):
    order = sanitize(order)
    if not order.is_valid:
        raise InvalidOrder

    inventory.reserve(order.items)
    payments.charge(order.customer, order.total)

    notifications.send(order.customer, "confirmed")
    audit.record(order)
```

## `presentation/declare-at-use`

```python
# bad: result is declared far from meaning
result = None
prepare()
validate()
result = compute(input)

# good: result appears when it becomes useful
prepare()
validate()
result = compute(input)
```

## `presentation/comments-explain-why`

```python
# bad: repeats the code
# increment attempts by one
attempts += 1

# good: explains the constraint
# Provider counts the first send as retry zero.
attempts += 1
```

## `simplification/delete-dead-code`

```python
# bad: the inner branch cannot run
def process(items):
    if not items:
        return
    for item in items:
        if not items:
            break
        handle(item)

# good
def process(items):
    if not items:
        return
    for item in items:
        handle(item)
```

## `simplification/no-flappy-booleans`

```go
// bad
if user.Enabled && user.EmailVerified {
    return true
}
return false

// good
return user.Enabled && user.EmailVerified
```

## `simplification/trivial-value-branch`

```python
# bad
def path_for(url):
    if url is None:
        return None
    return url.path

# good
def path_for(url):
    return None if url is None else url.path
```

## `simplification/inline-trivial-temps`

```python
# bad
hungry = is_hungry()
ripe = bananas_are_ripe()
should_pick = hungry and ripe
return should_pick

# good
return is_hungry() and bananas_are_ripe()
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

## `errors/check-every-return`

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

## `errors/no-swallowed-exceptions`

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

## `bugs/binary-chop`

```text
Bug: parser fails on a large input.

1. Test the first half and second half.
2. Keep the failing half.
3. Repeat until the offending input is isolated.

The same shape works for commits, config flags, and dependency versions.
```

## `bugs/root-cause-not-symptom`

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

## `tests/arrange-act-assert`

```python
def test_uppercase_capitalizes_every_letter():
    sentence = "this string should be uppercase."

    result = sentence.upper()

    assert result == "THIS STRING SHOULD BE UPPERCASE."
```

## `tests/spec-style-names`

```python
# bad
def test_list_1(): ...
def test_list_2(): ...

# good
def test_new_list_is_empty(): ...
def test_appending_increments_size(): ...
```

## `tests/no-implementation-mirror`

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

## `tests/test-doubles`

```python
# bad: touches real infrastructure
def test_user_lookup():
    db = connect("postgres://prod-replica")
    assert lookup(db, 42).name == "Ada"

# good: injects a small fake boundary
class StubDB:
    def fetch(self, user_id):
        return {"id": 42, "name": "Ada"}

def test_user_lookup():
    assert lookup(StubDB(), 42).name == "Ada"
```

## `complexity/break-cycles`

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

## `complexity/api-prevents-misuse`

```python
# bad: caller can forget cleanup
file = open_file(path)
read(file)

# good: correct cleanup is part of the call shape
with open_file(path) as file:
    read(file)
```

## `version-control/clear-messages`

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

## `collaboration/actionable-review`

```text
weak:
  This is confusing.

useful:
  `timeoutMs` is passed as seconds here, so callers using the documented
  millisecond value wait 1000x longer. Rename the parameter or convert
  before calling `setTimeout`.
```
