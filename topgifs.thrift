struct Gif {
  1: string gif_id,
  2: string url,
  3: string description,
  4: i32 count
}

service TopGifsService {
	Gif fetchGif(1:string gif_id)
}
