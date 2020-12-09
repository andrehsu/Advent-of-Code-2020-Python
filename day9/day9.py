INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def part1(inp: list[str], preamble_length=25) -> None:
    nums = list(map(int, inp))
    for i in range(preamble_length, len(nums)):
        if not is_sum_in(nums[i - preamble_length:i], nums[i]):
            print(nums[i])
            return


def part2(inp: list[str], preamble_length=25) -> None:
    nums = list(map(int, inp))
    desired_num = next(
        nums[i]
        for i in range(preamble_length, len(nums))
        if not is_sum_in(nums[i - preamble_length:i], nums[i])
    )
    for i in range(len(nums) - 1):
        section_sum = nums[i]
        for j in range(i + 1, len(nums)):
            section_sum += nums[j]
            if section_sum > desired_num:
                break
            elif section_sum == desired_num:
                section = nums[i: j + 1]
                print(min(section) + max(section))
                return


def is_sum_in(nums: list[int], desired: int):
    s = set(nums)
    for num in nums:
        if (desired - num) in s:
            return True
    
    return False


if __name__ == '__main__':
    print('Tests:')
    part1(TEST, 5)
    part2(TEST, 5)
    print('Solutions:')
    part1(INPUT)
    part2(INPUT)
