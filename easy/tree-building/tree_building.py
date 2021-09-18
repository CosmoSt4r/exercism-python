"""
Solution to Tree Building task on Exercism.

https://exercism.org/tracks/python/exercises/tree-building
"""

from __future__ import annotations


class Record(object):
    """Class for records."""

    def __init__(self, record_id: int, parent_id: int):
        """
        Initialize Record object.

        Args:
            record_id (int): record's identificator.
            parent_id (int): id of record's parent.

        """
        self.id_: int = record_id
        self.parent_id: int = parent_id

    def validate(self) -> Record:
        """
        Chek record for errors.

        Raises:
            ValueError: record is root and has a parent,
            ValueError: record's id is greater than parent's id,
            ValueError: parent's id is equal to record's id.

        Returns:
            Record: current instance.

        """
        if self.id_ == 0 and self.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
        if self.id_ < self.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if self.id_ == self.parent_id and self.id_ != 0:
            raise ValueError('Tree is a cycle')
        return self


class Node(object):
    """Class for tree nodes."""

    def __init__(self, node_id: int):
        """
        Initialize Node object.

        Args:
            node_id (int): node's id.

        """
        self.node_id: int = node_id
        self.children: list = []


def build_nodes(records: list) -> list:
    """
    Build list of Nodes from list of Records.

    Args:
        records (list): list of Record objects.

    Raises:
        ValueError: records' ids are not continuos.
        ValueError: first record's id is not 0.

    Returns:
        list: list of Node objects.

    """
    records.sort(key=lambda record: record.id_)
    if records[-1].id_ != len(records) - 1:
        raise ValueError('Tree must be continuous')
    if records[0].id_ != 0:
        raise ValueError('Tree must start with id 0')

    return [Node(record.validate().id_) for record in records]


def BuildTree(records: list) -> Node:
    """
    Build tree from Records list.

    Args:
        records (list): list of Record objects.

    Returns:
        Node: root node of the resulting tree.

    """
    if not records:
        return None
    nodes: list = build_nodes(records)

    for node in nodes:
        node.children = [
            nodes[record.id_]
            for record in records[1:]
            if record.parent_id == node.node_id
        ]
    return nodes[0]
