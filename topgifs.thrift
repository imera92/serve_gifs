struct Gif {
  1: i32 gif_id,
  2: string url,
  3: string description,
  4: i32 count
}

service TopGifsService {
	set<string> fetchGif(1:string gif_id)
}
