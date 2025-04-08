In Autosubmit, we currently use a decorator to document the types,
so that the decorator can be used as a way to fetch the description
of the types.

The issue with that, is that that probably isn't discarded in optimized
mode (that -O), and it can lead to memory issues if it's not implemented
well.

A better approach would be to use just plain docstrings.

While it requires a library or custom code to parse the docstrings
(wish Python stdlib would provide a parser?), there is an existing
and well-written library. Even if that library is not the most actively
maintained, the code looks "done" (in the sense that there isn't much else
to do, and bugs might be scarce, few).

Running python interpreter in production can then discard the comments,
and there is less risks of code bugs in the decorator implementation.

