function array = radix_sort(array)
%% Constants
max_array = max(array);
base = 1;

%% While Loop
while max_array/base > 0 %while max number greater than 1
    array = counting_sort(array,base); %call counting sort
    base = base * 10; %base multiply by 10
end

         function B = counting_sort(array,base) %counting sort
         C = zeros(1,11);
         B = zeros(1,numel(array));
         for j = 1:numel(array)
             C(rem(floor(array(j)/base),10)+1) = C(rem(floor(array(j)/base),10)+1) + 1;
         end
         for i = 2:11
            C(i) = C(i) + C(i-1);
         end
         for j = numel(array):-1:1
             B(C(rem(floor(array(j)/base),10)+1)) = array(j);
             C(rem(floor(array(j)/base),10)+1) = C(rem(floor(array(j)/base),10)+1) - 1;
         end
     end
end 