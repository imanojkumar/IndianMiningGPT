"""
IndianMiningGPT

FAISS Manager

Lazy loads:
- FAISS Index
- Chunk Metadata
"""

from pathlib import Path

import faiss
import pandas as pd


class FaissManager:

    _index = None
    _chunk_registry = None

    @classmethod
    def index(cls):

        if cls._index is None:

            print(
                "\nLoading FAISS Index..."
            )

            project_root = (
                Path(__file__)
                .resolve()
                .parents[2]
            )

            index_path = (
                project_root
                / "data"
                / "processed"
                / "faiss"
                / "faiss.index"
            )

            cls._index = faiss.read_index(
                str(index_path)
            )

            print(
                f"Vectors: {cls._index.ntotal}"
            )

        return cls._index

    @classmethod
    def chunk_registry(cls):

        if cls._chunk_registry is None:

            print(
                "\nLoading Chunk Registry..."
            )

            project_root = (
                Path(__file__)
                .resolve()
                .parents[2]
            )

            registry_path = (
                project_root
                / "data"
                / "processed"
                / "chunk_metadata"
                / "chunk_registry.csv"
            )

            cls._chunk_registry = (
                pd.read_csv(
                    registry_path
                )
            )

            print(
                "Chunk Metadata Rows:",
                len(
                    cls._chunk_registry
                )
            )

        return cls._chunk_registry
