# encoding = 'utf-8'

import random


class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_lvl, P):
        self.MAXLVL = max_lvl
        self.P = P
        self.header = self.createNode(self.MAXLVL, -1)
        self.level = 0

    def createNode(self, lvl, key):
        return Node(key, lvl)

    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAXLVL:
            lvl += 1
        return lvl

    def insert(self, key):
        key = int(key)
        update = [None] * (self.MAXLVL + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            rlevel = self.randomLevel()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            n = self.createNode(rlevel, key)
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

    def search(self, key):
        key = int(key)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return True
        return False

    def displayList(self):
        print("Printing Skip List:")
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.header.forward[lvl]
            while node:
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")
