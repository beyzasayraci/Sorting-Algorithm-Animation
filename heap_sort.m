function array = heap_sort(array)
    heap_size = numel(array); %array size
    array = build_max_heap(array,heap_size); %calling function
    for i = numel(array):-1:2 
        array([i 1]) = array([1 i]); %swap
        heap_size = heap_size - 1; 
        array = max_heapify(array,heap_size,1);
    end
end

function array = build_max_heap(array,heap_size) 
    for i = floor(heap_size/2):-1:1
        array = max_heapify(array,heap_size,i); %call function max_heapify
    end
end

function array = max_heapify(array,heap_size,i)
    l = left(i); %lef side
    r = right(i); %right side
    if l <= heap_size && array(l) > array(i)
        largest = l; %make largest equal to 1
    else
        largest = i; %make largest equal to i
    end
    if r <= heap_size && array(r) > array(largest)
        largest = r; %make largest equal to r
    end
    if largest ~= i %if largest is not equal i
        array([largest i]) = array([i largest]); %swap between array(largest) and array(i)
        array = max_heapify(array,heap_size,largest); %call function max_heapify
    end
end

function l = left(i)
    l = 2 * i;
end

function r = right(i)
    r = 2 * i + 1;
end