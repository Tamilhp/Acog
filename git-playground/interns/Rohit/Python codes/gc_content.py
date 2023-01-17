def gc_content(seq):
    for i in range(len(user_list)):
        Count_C = len([j for j in user_list[i] if j == 'C'])
        Count_G = len([j for j in user_list[i] if j == 'G'])
        total_count = Count_C + Count_G
        total_seq = len(user_list[i])

        gccount = (total_count/total_seq)*100
        print(gccount)
        op_list = [gccount]

    for k in range(len(op_list)):            
        result = max(op_list)
    print(result)


if __name__ == "__main__":
    input_seq = input('Enter elements of a list separated by space ')
    user_list = input_seq.split()
    print(user_list)
    gc_content(user_list)




     
#gc_content("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT") 
