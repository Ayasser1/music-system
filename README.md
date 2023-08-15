#  Music PlayList

  ## Database Model
  ### playlist table
  - id -> uuid
  - title -> playlist name
  - moods -> mtm relation to have all moods for filtering
  - genres -> mtm relation to have all genres for filtering
  - created_at -> time added
  - updated_at -> time modified
  ### playlist_track
  - id -> uuid
  - playlist_id -> fk for playlist table
  - track_id -> fk for track table
  - is first -> first track in the playlist
  - next_playlist_track -> fk to playlist_track to get next track

  #### Explaint
    Modeling playlist_track table to be like linked list where it's more accsible to build playlist and re-order it.
   
## API
  - GET     /playlist/:pk/
    get playlist returning serlized data of playlist
  
  - LIST    /playlist/?page=
    listing with pagination for playlists
  
  - POST    /playlist/ -> request body -> {title: string}
    create playlist
  
  - DELETE  /playlist/:pk/
    delete playlist
  
  - LIST    /playlist/?playlist_id=uuid
    get tracks of the playlist by id
  
  - DELETE  /playlist_track/:pk/
    delete track from playlist with keeping the order
  
  - PATCH   /playlist_track/:pk/  -> request body -> {'next_playlist_track_id': uuid}
    reorder the track by using uuid of track_playlist as pk and the next track after next_playlist_track_id 
  
  - GET     /playlist_track/:pk/  
    get playlist details

## things to be done if i have time:
  - Swagger file
  - Unit test
  - docker for unit test.
  - pipeline (exp github action).
  - more code sepration.
  - More docs

