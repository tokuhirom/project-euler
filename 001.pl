use 5.018000;
use List::Util qw(reduce);

say reduce { $a + $b } grep { ($_ % 3==0) || ($_ % 5 == 0) } 1..1000-1;
