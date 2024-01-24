import os
import numpy as np

class BatchRename:
    """ Override the get_new_path and get_curr_paths functions """
    def __init__(self) -> None:
        pass

    def get_curr_paths(curr_dir):
        curr_fns = sorted(os.listdir(curr_dir))
        curr_fp = []
        for curr_fn in  curr_fns:
            curr_fp.append(curr_dir, curr_fn)
        return np.array(curr_fp)

    def get_new_path(curr_dir, curr_fn):
        tgt_dir = curr_dir
        tgt_fn = curr_fn
        new_path = os.path.join(tgt_dir, tgt_fn)
        return new_path

    def rename(curr_path, new_path):
        command = f"mv {curr_path} {new_path}"
        os.system(command)

    def main(self, curr_dir):
        curr_fps = self.get_curr_paths(curr_dir)
        for curr_fp in curr_fps:
            new_fp = self.get_new_path(curr_dir, curr_fp)
            self.rename(curr_fp, new_fp)

### Example Usage
if __name__ == "__main__":
    class MyBatchRename(BatchRename):
        def __init__(self) -> None:
            super().__init__()
        def get_curr_paths(curr_dir):
            return super().get_curr_paths()
        def get_new_path(curr_dir, curr_fn):
            return super().get_new_path(curr_fn)
