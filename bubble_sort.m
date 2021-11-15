%EGE ALP TÜRKYENER
function bubble_sort = bubble_sort(array)
for i=1:length(array)-1
    for j=length(array):-1:i+1
       
        if array(j)>array(j-1)
            key=array(j-1);%saving our number in a constant
            array(j-1)=array(j);%replacing numbers in the array
            array(j)=key;%replacing numbers in the array
        end
    end
end
bubble_sort=array;
