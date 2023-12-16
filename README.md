# ruff-0.1.8-bug

```console
┌─────────────────────────────────────────────────────────── 2023-12-17 00:41:51
│ DW-Mac derek .../ruff-0.1.8-bug  master ? ! +4-1
│ 🐍 3.10.13
└ ❯ which ruff
/opt/homebrew/bin/ruff

┌─────────────────────────────────────────────────────────── 2023-12-17 00:41:57
│ DW-Mac derek .../ruff-0.1.8-bug  master ? ! +4-1
│ 🐍 3.10.13
└ ❯ ruff --version
ruff 0.1.8

┌─────────────────────────────────────────────────────────── 2023-12-17 00:42:01
│ DW-Mac derek .../ruff-0.1.8-bug  master ? ! +4-1
│ 🐍 3.10.13
└ ❯ ruff --unsafe-fixes --fix .
error: Panicked while linting test.py: This indicates a bug in Ruff. If you could open an issue at:

    https://github.com/astral-sh/ruff/issues/new?title=%5BLinter%20panic%5D

...with the relevant file contents, the `pyproject.toml` settings, and the following stack trace, we'd be very appreciative!

panicked at /private/tmp/ruff-20231213-5372-n34weh/ruff-0.1.8/crates/ruff_text_size/src/range.rs:48:9:
assertion failed: start.raw <= end.raw
Backtrace:    0: std::backtrace::Backtrace::force_capture
   1: ruff_cli::panic::catch_unwind::{{closure}}
   2: std::panicking::rust_panic_with_hook
   3: std::panicking::begin_panic_handler::{{closure}}
   4: std::sys_common::backtrace::__rust_end_short_backtrace
   5: _rust_begin_unwind
   6: core::panicking::panic_fmt
   7: core::panicking::panic
   8: ruff_linter::linter::lint_fix
   9: ruff_cli::commands::check::check::{{closure}}
  10: rayon::iter::plumbing::bridge_producer_consumer::helper
  11: rayon_core::join::join_context::{{closure}}
  12: <rayon_core::job::StackJob<L,F,R> as rayon_core::job::Job>::execute
  13: rayon_core::registry::WorkerThread::wait_until_cold
  14: std::sys_common::backtrace::__rust_begin_short_backtrace
  15: core::ops::function::FnOnce::call_once{{vtable.shim}}
  16: std::sys::unix::thread::Thread::new::thread_start
  17: __pthread_joiner_wake


```