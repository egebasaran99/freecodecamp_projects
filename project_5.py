def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),
        [],
        []
    ]

    moves = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def move_disks(disks, source, target, auxiliary):
        if disks == 0:
            return

        # Move the top n - 1 disks to the auxiliary rod
        move_disks(disks - 1, source, auxiliary, target)

        # Move the largest remaining disk to the target rod
        disk = rods[source].pop()
        rods[target].append(disk)

        # Record the arrangement after the move
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

        # Move the n - 1 disks from auxiliary to target
        move_disks(disks - 1, auxiliary, target, source)

    move_disks(n, 0, 2, 1)

    return "\n".join(moves)