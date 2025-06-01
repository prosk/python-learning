def generate_brackets():
    n = int(input())
    generate_all_seq("", 0, 0, n)


def generate_all_seq(curr_seq, curr_left, curr_right, n):
    if len(curr_seq) == 2 * n:
        print(curr_seq)
    else:
        if curr_left == curr_right:
            generate_all_seq(curr_seq + "(", curr_left + 1, curr_right, n)
        elif curr_left > curr_right:
            if curr_left < n:
                generate_all_seq(curr_seq + "(", curr_left + 1, curr_right, n)
                generate_all_seq(curr_seq + ")", curr_left, curr_right + 1, n)
            else:
                generate_all_seq(curr_seq + ")", curr_left, curr_right + 1, n)


if __name__ == '__main__':
    generate_brackets()
