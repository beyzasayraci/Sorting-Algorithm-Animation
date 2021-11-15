%EGE ALP TÜRKYENER
function insertion_sort = insertion_sort(array)%creating function for insertion sort.
for j=2:length(array)%for the numbers from 2 to len(array)

    key=array(j);%save A[j element to a temporary constant.

    i=j-1;
   % move the elements of array A if
   %it is greater than key.
    while i>0 && array(i)>key
        array(i+1)=array(i);
        i=i-1;
        array(i+1)=key;    
    end
end
insertion_sort = array;