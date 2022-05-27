import os
os.system("pip install -U loompy")

import scanpy as sc
import anndata
import loompy

adata = sc.read_loom('GSE186068_gene-count.loom')
adata.obs