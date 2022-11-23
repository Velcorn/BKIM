import rpy2.robjects as r
from rpy2.robjects.packages import importr


utils = importr('utils')
utils.install_packages('BiocManager')
utils.chooseBioCmirror(ind=1)