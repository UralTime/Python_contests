var
n:longword;
x:array of longword;
xx:array of real;
v:array of longword;
i,j,indexmaks,indexmin:longword;
l,r,m,maks,min:real;
begin
Readln(n);
Setlength(x,n);
Setlength(v,n);
for i:=0 to n-1 do
    begin
    Readln(x[i],v[i]);
    end;
l := 0;
r := 20000000;
for j:=0 to 200 do
    begin
    m := (r + l) / 2;
    Setlength(xx,n);
    xx[0] := x[0] + v[0] * m;
    maks := xx[0];
    indexmaks := 0;
    min := xx[0];
    indexmin := 0;
    for i:=1 to n-1 do
        begin
        xx[i] := x[i] + v[i] * m;
        if xx[i] > maks then
            begin
            maks := xx[i];
            indexmaks := i;
            end;
        if xx[i] < min then
            begin
            min := xx[i];
            indexmin := i;
            end;
        end;
    if v[indexmin] > v[indexmaks] then
        l := m
    else
        r := m;
    end;
print(l, maks - min);
end.
