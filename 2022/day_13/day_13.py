import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_13.txt") as file:
    packets = [line.strip() for line in file.readlines()]

packets_edit = []

curr_packet = []
for i, packet in enumerate(packets):

    if packet == "" :
        packets_edit.append(curr_packet)
        curr_packet = []
    else:
        packet = eval(packet)
        curr_packet.append(packet)

    if i == len(packets) - 1:
        packets_edit.append(curr_packet)
        curr_packet = []
correct_index_list = []

def compare_packets(packet1, packet2):
    is_1_int = isinstance(packet1, int)
    is_2_int = isinstance(packet2, int)

    if is_1_int and is_2_int:
        if packet1 < packet2:
            return True
        elif packet1 > packet2:
            return False
        else:
            return None

    if not is_1_int and not is_2_int:
        for p1, p2 in zip(packet1, packet2):
            return_val = compare_packets(p1, p2)
            if return_val is not None:
                return return_val
        if len(packet1) == len(packet2):
            return None
        if len(packet1) > len(packet2):
            return False
        if len(packet1) < len(packet2):
           return True


    if is_1_int and not is_2_int:
        return compare_packets([packet1], packet2)
    elif not is_1_int and is_2_int:
        return compare_packets(packet1, [packet2])

        


    
            
for i, packet_pair in enumerate(packets_edit):
    packet1 = packet_pair[0]
    packet2 = packet_pair[1]
    correct = compare_packets(packet1, packet2)
    if correct:
        correct_index_list.append(i + 1)
        
print("Part 1: " + str(sum(correct_index_list)))

# Part 2
packets_full_list = []
packet1_index_counter = 1
packet2_index_counter = 2
for packet_pair in packets_edit:
    packets_full_list.append(packet_pair[0])
    packets_full_list.append(packet_pair[1])

for i, packet in enumerate(packets_full_list):
    packet1 = [[2]]
    packet2 = [[6]]
    correct1 = compare_packets(packet, packet1)
    correct2 = compare_packets(packet, packet2)
    if correct1:
        packet1_index_counter += 1
    if correct2:
        packet2_index_counter += 1
print("Part 2: " + str(packet1_index_counter * packet2_index_counter))

