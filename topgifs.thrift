service TopGifsService {
	set<string> fetchGif(1:string gif_id)
	set< set<string>> fetchAllGifs()
}
