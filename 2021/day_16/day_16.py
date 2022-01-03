import numpy as np
#https://www.alpharithms.com/python-convert-hexadecimal-to-binary-111821/
def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
    """
    Converts a hexadecimal value into a string representation
    of the corresponding binary value
    Args:
        hex_number: str hexadecimal value
        num_digits: integer value for length of binary value.
                    defaults to 8
    Returns:
        string representation of a binary number 0-padded
        to a minimum length of <num_digits>
    """
    return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)

# hex_string: input
hex_string = "005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840"

bin_string = ""
for character in hex_string:
    bin_string += hex_to_binary(character, 4)

sum_version_numbers = 0

def parse_literal_value(binary_string):
    packet_version = int(binary_string[0:3],2)
    global sum_version_numbers
    sum_version_numbers += packet_version
    packet_type_id = int(binary_string[3:6],2)
    binary_string = binary_string[6:]
    if packet_type_id == 4: #literal value
        literal_value = ""
        while True:
            first_bin = binary_string[0]
            four_bin = binary_string[1:5]
            binary_string = binary_string[5:]
            if first_bin == "1":
                literal_value += four_bin
            elif first_bin == "0":
                literal_value += four_bin
                break
        return int(literal_value,2), binary_string
    else:
        length_type_id = binary_string[0]
        value_of_current_packet = 0
        values_of_subpackets = []
        if length_type_id == "0":
            length_of_subpackets = int(binary_string[1:16],2)
            total_length = 0
            binary_string = binary_string[16:]
            while total_length < length_of_subpackets:
                length_before = len(binary_string)
                value_of_subpacket, binary_string = parse_literal_value(binary_string)
                length_of_packet = length_before - len(binary_string)
                total_length += length_of_packet
                values_of_subpackets.append(value_of_subpacket)
        elif length_type_id == "1":
            n_subpackets = int(binary_string[1:12],2)
            binary_string = binary_string[12:]
            for _ in range(n_subpackets):
                value_of_subpacket, binary_string = parse_literal_value(binary_string)
                values_of_subpackets.append(value_of_subpacket)
               
        if packet_type_id == 0:
            value_of_current_packet = sum(values_of_subpackets)
        elif packet_type_id == 1:
            value_of_current_packet = np.prod(values_of_subpackets)
        elif packet_type_id == 2:
            value_of_current_packet = min(values_of_subpackets)
        elif packet_type_id == 3:
            value_of_current_packet = max(values_of_subpackets)
        elif packet_type_id == 5: # value_of_current_packet = 1 if values_of_subpackets[0] < values_of_subpackets[1] else 0
            if values_of_subpackets[0] > values_of_subpackets[1]:
                value_of_current_packet = 1
            else:
                value_of_current_packet = 0
        elif packet_type_id == 6:
            value_of_current_packet = 1 if values_of_subpackets[0] < values_of_subpackets[1] else 0
        elif packet_type_id == 7:
            value_of_current_packet = 1 if values_of_subpackets[0] == values_of_subpackets[1] else 0
        return value_of_current_packet, binary_string

total_value, _ = parse_literal_value(bin_string)
print('Part 1:', sum_version_numbers)
print('Part 2:', total_value)
