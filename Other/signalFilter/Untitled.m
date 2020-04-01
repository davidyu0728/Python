[m,n] = size(S0);
for i = 1:100
   a = S0(i,:)';
   plot(a);
   hold on;
end