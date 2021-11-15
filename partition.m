function [arr, i ] = partition(arr, low, high)

pivot = arr(high); %pivot is last of the array

i = low -1; 
for j = low:high-1 
    if arr(j)<=pivot %if pivot bigger than array's j item
        i = i+1; %i is increased by 1
        if i~=j %if i is not equal j
                key = arr(i); %swap arr(i) and arr(j)
                arr(i) = arr(j);
                arr(j) = key;
        end
    end
end
    i = i+1; %i is increased by 1
    key = arr(i); %swap arr(i) and arr(high)
    arr(i) = arr(high);
    arr(high) = key;
end