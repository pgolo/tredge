import sys; sys.path.insert(0, '')
import unittest
import tredge # pylint: disable=E0611,F0401

class TestQTred(unittest.TestCase):

    def test_no_tredge_dict_str(self):
        g = {
            'b': set(['a']),
            'c': set(['a']),
            'd': set(['b', 'c']),
            'e': set(['d'])
        }
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_dict_int(self):
        g = {
            2: set([1]),
            3: set([1]),
            4: set([2, 3]),
            5: set([4])
        }
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_list_str(self):
        g = [
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd')
        ]
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_list_int(self):
        g = [
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4)
        ]
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_tuple_str(self):
        g = (
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd')
        )
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_tuple_int(self):
        g = (
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4)
        )
        result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_no_tredge_file(self):
        with open('test/assets/test_no_tredge.tab', mode='r', encoding='utf8') as g:
            result = tredge.transitive_edges(g)
        expected = set()
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_dict_str(self):
        g = {
            'b': set(['a']),
            'c': set(['a']),
            'd': set(['b', 'c', 'a']),
            'e': set(['d'])
        }
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_dict_int(self):
        g = {
            2: set([1]),
            3: set([1]),
            4: set([2, 3, 1]),
            5: set([4])
        }
        result = tredge.transitive_edges(g)
        expected = set([(4, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_list_str(self):
        g = [
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('d', 'a')
        ]
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_list_int(self):
        g = [
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (4, 1)
        ]
        result = tredge.transitive_edges(g)
        expected = set([(4, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_tuple_str(self):
        g = (
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('d', 'a')
        )
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_tuple_int(self):
        g = (
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (4, 1)
        )
        result = tredge.transitive_edges(g)
        expected = set([(4, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_1_hop_file(self):
        with open('test/assets/test_1_tredge_1_hop.tab', mode='r', encoding='utf8') as g:
            result = tredge.transitive_edges(g)
        expected = set([('d', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_dict_str(self):
        g = {
            'b': set(['a']),
            'c': set(['a']),
            'd': set(['b', 'c']),
            'e': set(['d', 'a'])
        }
        result = tredge.transitive_edges(g)
        expected = set([('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_dict_int(self):
        g = {
            2: set([1]),
            3: set([1]),
            4: set([2, 3]),
            5: set([4, 1])
        }
        result = tredge.transitive_edges(g)
        expected = set([(5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_list_str(self):
        g = [
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('e', 'a')
        ]
        result = tredge.transitive_edges(g)
        expected = set([('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_list_int(self):
        g = [
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (5, 1)
        ]
        result = tredge.transitive_edges(g)
        expected = set([(5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_tuple_str(self):
        g = (
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('e', 'a')
        )
        result = tredge.transitive_edges(g)
        expected = set([('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_tuple_int(self):
        g = (
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (5, 1)
        )
        result = tredge.transitive_edges(g)
        expected = set([(5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_1_tredge_2_hops_file(self):
        with open('test/assets/test_1_tredge_2_hops.tab', mode='r', encoding='utf8') as g:
            result = tredge.transitive_edges(g)
        expected = set([('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_dict_str(self):
        g = {
            'b': set(['a']),
            'c': set(['a']),
            'd': set(['b', 'c', 'a']),
            'e': set(['d', 'a'])
        }
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a'), ('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_dict_int(self):
        g = {
            2: set([1]),
            3: set([1]),
            4: set([2, 3, 1]),
            5: set([4, 1])
        }
        result = tredge.transitive_edges(g)
        expected = set([(4, 1), (5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_list_str(self):
        g = [
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('e', 'a'),
            ('d', 'a')
        ]
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a'), ('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_list_int(self):
        g = [
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (5, 1),
            (4, 1)
        ]
        result = tredge.transitive_edges(g)
        expected = set([(4, 1), (5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_tuple_str(self):
        g = (
            ('b', 'a'),
            ('c', 'a'),
            ('d', 'b'),
            ('d', 'c'),
            ('e', 'd'),
            ('e', 'a'),
            ('d', 'a')
        )
        result = tredge.transitive_edges(g)
        expected = set([('d', 'a'), ('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_tuple_int(self):
        g = (
            (2, 1),
            (3, 1),
            (4, 2),
            (4, 3),
            (5, 4),
            (5, 1),
            (4, 1)
        )
        result = tredge.transitive_edges(g)
        expected = set([(4, 1), (5, 1)])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

    def test_2_tredges_1_2_hops_file(self):
        with open('test/assets/test_2_tredges_1_2_hops.tab', mode='r', encoding='utf8') as g:
            result = tredge.transitive_edges(g)
        expected = set([('d', 'a'), ('e', 'a')])
        assert result == expected, 'Expected %s, got %s' % (str(expected), str(result))

if __name__ == '__main__':
    unittest.main()
