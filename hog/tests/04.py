test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_perfect_piggy(10)
          d763fd836a7bfb096222e985b161b406
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> is_perfect_piggy(1)
          d763fd836a7bfb096222e985b161b406
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> is_perfect_piggy(27)
          bc6c4798917b91886d7fa5f56e42878f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> is_perfect_piggy(81)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(121)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(34)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_perfect_piggy(64)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
