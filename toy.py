import fuse

class ToyStat(fuse.Stat):
    def __init__(self):
        """
        The following stat structure members are implemented.
        """
        self.st_mode  = 33206  # (protection bits)
        self.st_ino   = 0      # (inode number)
        self.st_dev   = 0      # (device)
        self.st_nlink = 0      # (number of hard links)
        self.st_uid   = 500    # (user ID of owner)
        self.st_gid   = 500    # (group ID of owner) 
        self.st_size  = 0      # (size of file, in bytes)
        self.st_atime = 0      # (time of most recent access)
        self.st_mtime = 0      # (time of most recent content modification)
        self.st_ctime = 0      # (time of most recent metadata change)

class Toy():
    def getattr(path):
        return ToyStat()

    def readdir(path):
        contents = {
            '/':      ['hello', 'world'],
            '/hello': ['monde'],
            '/hello/monde': ['last_level']
        }
        return contents.get(path, [])
        
