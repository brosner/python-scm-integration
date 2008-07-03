
class SourceBackend(object):
    def fetch_changesets(self):
        raise NotImplemented()

class Subversion(SourceBackend):
    pass

class Git(SourceBackend):
    pass
