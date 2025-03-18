# -- coding: UTF-8 --
 
 
def game_id_to_channel(game_id):
    dec_num = int(f"0x{game_id}", 16)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if dec_num == 0:
        return "0000"
    channel_id = ""
    while dec_num > 0:
        remainder = dec_num % 36
        channel_id = digits[remainder] + channel_id
        dec_num //= 36
    return channel_id.rjust(4, "0")

if __name__ == "__main__":
    print(game_id_to_channel("800703"))

    print("sf2 = " + game_id_to_channel("42982A"))
    print("sf2ce = " + game_id_to_channel("37377A"))
    print("sfzch = " + game_id_to_channel("64254A"))
    print("sf2hf = " + game_id_to_channel("37378A"))

    print("dino = " + game_id_to_channel("37360A"))
    print("captcomm = " + game_id_to_channel("37358A"))
    print("dynwar = " + game_id_to_channel("41078A"))
    print("ffight = " + game_id_to_channel("37362A"))
    print("3wonders = " + game_id_to_channel("37357A"))
    print("wof = " + game_id_to_channel("44111A"))
    print("1941 = " + game_id_to_channel("39873A"))
