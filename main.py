def subset_sum_with_axiomatic_filtering(nums, target):
    """
    Subset Sum Problem optimized with logical axiomatic pruning.
    This demonstrates how embedding mathematical axioms directly
    into the algorithm prevents unnecessary exponential branch exploration.
    """
    
    # Sort the array to easily calculate running minimums and maximums
    nums.sort()
    
    def backtrack(index, current_sum):
        # Base case: we reached the target
        if current_sum == target:
            return True
        
        # Out of bounds
        if index >= len(nums):
            return False
            
        # --- AXIOMATIC FILTERING LAYER ---
        remaining_nums = nums[index:]
        
        # Axiom 1: If all remaining numbers are positive and target is out of reach
        pos_sum = sum(x for x in remaining_nums if x > 0)
        if current_sum + pos_sum < target:
            return False # Instant prune! No need to check any subsets.
            
        # Axiom 2: If all remaining numbers are negative and we need a positive sum
        neg_sum = sum(x for x in remaining_nums if x < 0)
        if current_sum + neg_sum > target:
            return False # Instant prune!
        # ----------------------------------

        # Standard branching
        # 1. Include the current number
        if backtrack(index + 1, current_sum + nums[index]):
            return True
            
        # 2. Exclude the current number
        if backtrack(index + 1, current_sum):
            return True
            
        return False

    return backtrack(0, 0)

# Test the axiomatic logic
test_set = [-7, -3, -2, 5, 8]
target_value = 0
result = subset_sum_with_axiomatic_filtering(test_set, target_value)
print(f"Is there a subset that sums up to {target_value}? {result}")
