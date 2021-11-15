%EGE ALP TÜRKYENER
function array=merge_sort(array)
    array=mergesort(array,1,length(array));
end

function array = mergesort(array,first,last)%dividing the list into 2 halfes.
    if first < last
        mid = floor((first + last)/2); %finding middle index.
        array = mergesort(array,first,mid);
        array = mergesort(array,mid + 1,last);
        array = merge(array,first,mid,last); %combining sorted lists.
    end
end

function array = merge(array, first, mid, last)
    n1 = mid - first + 1; 
    n2 = last - mid;
    L = zeros(1, n1+1); %left side of list.
    R = zeros(1, n2+1); %right side of list.
    for i=1:n1
        L(i) = array(first+ i - 1);    
    end
    for j=1:n2
        R(j) = array(mid+j);
    end
    L(n1+1) = inf; %adding the last index  infinite number.
    R(n2+1) = inf;%adding the last index infinite number.
    i=1;
    j=1;
    
    for k=first:last
       
        if L(i)<=R(j) %comparison between righ and left side of lists and
        array(k)=L(i); %ordering them.
        i=i+1;
        
        else
            array(k)=R(j);
            j=j+1;
        end
    end
end
