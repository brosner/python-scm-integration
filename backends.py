
class SourceBackend(object):
    """
    A generic interface for different source control backends.
    """
    def fetch_changesets(self):
        raise NotImplemented()

class Subversion(SourceBackend):
    pass

class Git(SourceBackend):
    pass
