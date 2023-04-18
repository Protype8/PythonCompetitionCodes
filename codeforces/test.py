for position in buildable_list:
    temp_list = delivery_list.copy()
    temp_list.append(position)
    all_block_delivery_time = []
    for i in range(len(temp_list)):
        delviery_times = []
        for j in range(len(temp_list)):
            if (i != j):
                delivery_time = abs(temp_list[i][0] - temp_list[j][0]) + abs(temp_list[i][1] - temp_list[j][1])
                delviery_times.append(delivery_time)
        i_block_delivery_time = min(delviery_times)
        all_block_delivery_time.append(i_block_delivery_time)
    overall_delivery_time = max(all_block_delivery_time)
    overall_delviery_times.append(overall_delivery_time)
print(buildable_list)
print(overall_delviery_times)