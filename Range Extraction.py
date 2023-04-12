# A format for expressing an ordered list of integers is to use a comma separated list of either
#
#     individual integers
#     or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
#
# Example:
#
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


def solution(numbers):
  ranges = []
  start_range = None
  end_range = None

  for n in numbers:
      if start_range is None:
          start_range = n
          end_range = n
      elif n == end_range + 1:
          end_range = n
      else:
          if end_range - start_range >= 2:
              ranges.append(f"{start_range}-{end_range}")
          else:
              ranges.extend(str(i) for i in range(start_range, end_range + 1))
          start_range = n
          end_range = n

  if end_range - start_range >= 2:
      ranges.append(f"{start_range}-{end_range}")
  else:
      ranges.extend(str(i) for i in range(start_range, end_range + 1))

  return ",".join(ranges)