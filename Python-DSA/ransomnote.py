class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False

        ransomNote_hash_map = {}
        magazine_hash_map = {}

        for char in ransomNote:
            ransomNote_hash_map[char] = ransomNote_hash_map.get(char, 0) + 1

        for char in magazine:
            magazine_hash_map[char] = magazine_hash_map.get(char, 0) + 1

        for char, count in ransomNote_hash_map.items():
            if magazine_hash_map.get(char, 0) < count:
                return False

        return True
