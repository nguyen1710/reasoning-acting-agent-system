from analyzer import SystemAnalyzer

spec = """
Users can register accounts, log in, and edit personal information.
Administrators can approve new users, block offending accounts.
Both can create posts, comment, and rate other posts.
"""

agent = SystemAnalyzer()
result = agent.analyze(spec)
print(result)

# result
# {'actors': ['User', 'Admin'], 
#  'functions': ['Register account', 'Login', 'Edit personal information', 'Approve new users', 'Block violating accounts', 'Create post', 'Comment', 'Rate posts'], 
#  'relationships': [{'actor': 'User', 'function': 'Register account', 'target': 'System'}, {'actor': 'User', 'function': 'Login', 'target': 'System'}, {'actor': 'User', 'function': 'Edit personal information', 'target': 'Own account'}, {'actor': 'Admin', 'function': 'Approve new users', 'target': 'User accounts'}, {'actor': 'Admin', 'function': 'Block violating accounts', 'target': 'User accounts'}, {'actor': 'User', 'function': 'Create post', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Create post', 'target': 'Content'}, {'actor': 'User', 'function': 'Comment', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Comment', 'target': 'Content'}, {'actor': 'User', 'function': 'Rate posts', 'target': 'Content'}, {'actor': 'Admin', 'function': 'Rate posts', 'target': 'Content'}]
# }
