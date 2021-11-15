function array = bucket_sort(array)
    %% Constants
    max_array = max(array); %find max array
    bucket = zeros(1,max_array+1); %create bucket
   %% For Loop
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
    end
    index = 1;
    for i = 1:max_array+1
        for j = 1:bucket(i) 
            array(index) = i;
            index = index + 1;
        end
    end
end
