import sys,pathlib
curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent
sys.path.append(home_dir.as_posix())

from src.data.make_dataset import IndianFundingDataAnalysis
