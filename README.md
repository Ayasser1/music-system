#  Music PlayList

  ## Database Model
  ### `playlist` table
  | key | Description | type|
  | -- | -- | -- |
  | id | unique ID | UUID |
  | title | Playlist Name | string |
  | moods | mtm relation to having all moods for filtering  | list of foreign keys |
  | genres | mtm relation to having all genres for filtering | list of foreign keys |
  | created_at | time added | timezone format |
  | updated_at | time modified | timezone format |
  ###  `playlist_track` table
  | key | Description | type|
  | -- | -- | -- |
  | id | unique ID | UUID |
  | playlist_id | foreign key of playlist id reference unique with track_id | UUID |
  | track_id | foreign key of playlist id reference unique with track_id | UUID |
  | is_first | first track in the playlist, default False | Boolean |
  | next_playlist_track | fk to playlist_track to get next track | UUID |

  #### Explaint
    Modeling playlist_track table to be a linked list where it's more accessible to build a playlist and re-order it.
   
## API
  | Request Method | url | Description | 
  | -- | -- | -- |
  | GET | /playlist/:pk/ | get playlist returning serialized data of playlist |
  | LIST | /playlist/?page=int |  listing with pagination for playlists |
  | POST | /playlist/ |  request body -> {title: string}, create playlist |
  | DELETE | /playlist/:pk/ | delete playlist |
  | LIST  | /playlist/?playlist_id=uuid | get tracks of the playlist by id | 
  | DELETE | /playlist_track/:pk/ | Delete the track from the playlist with keeping the order |
  | PATCH | /playlist_track/:pk/ |  request body -> {'next_playlist_track_id': uuid} |reorder the track by using UUID of track_playlist as pk and the next track after next_playlist_track_id |
  | GET | /playlist_track/:pk/ | get playlist details |

## Things to be done if I have time:
  - Swagger file
  - Unit test
  - docker for unit test.
  - pipeline (exp github action).
  - more code sepration.
  - More docs

