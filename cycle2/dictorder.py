sample_dict={'apple':5,'banana':3,'cherry':10,'dates':7}
ascending_order=dict(sorted(sample_dict.items()))
descending_order=dict(sorted(sample_dict.items(),reverse=True))
print("Dictionary sorted in ascending order:",ascending_order)
print("Dictionary sorted in descending order:",descending_order)
