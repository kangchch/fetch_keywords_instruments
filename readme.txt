medical_instruments
国产机械表
medical_instruments_tbl
{
	keywords
	status 0 为抓取 1 抓取
	page 目前是根据已知页面的页数先存到库里
	insert_time
	update_time
}

进口机械表
medical_instruments_import_tbl
{
	keywords
	status 0 未抓取 1 抓取
	page 
	insert_time
	update_time
}

在抓进口时，在正则前面加了一句，encode('utf-8')就好了。
线上机器和测试机器的mongodb配置可能不同，由处理正则表现出来。