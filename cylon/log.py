import sys

#sys.tracebacklimit = 0


class log:

    @classmethod
    def fail(cls, actual="", expect="", message=""):
        content = ""

        if actual or expect:
            content = "actual: '%s' \nexpect: '%s'" % (actual, expect)
        if message:
            content += "\nmessage: %s" % (message)

        print(content)
        raise RuntimeError("Test step failed.")
