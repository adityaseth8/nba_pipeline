api --> s3 raw data --> glue crawler --> aws glue data catalog --> aws athena  
&emsp;&emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; ^  
&emsp;&emsp;&emsp;&emsp;&emsp;        -- > glue job --> s3 clean data --> data crawler |
