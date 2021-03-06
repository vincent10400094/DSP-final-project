import numpy as np
import argparse

from utility import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('vocabulary_path', type=str, help='Input vocabulary file')
    parser.add_argument('document_path', type=str, help='Input document file')
    args = parser.parse_args()

    vocab_map, t = build_vocabulary_map(args.vocabulary_path)
    documents = read_documents(args.document_path)
    W = build_document_matrix(vocab_map, documents, t)
    np.save('W', W)