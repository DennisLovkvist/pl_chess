create or replace package Test as 

function PLAYER_EXISTS( PLAYER_ID_I PLAYER.PLAYER_ID%type)RETURN number;
function VALIDATE_MOVE_PAWN(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number,
                                INVERT_Y_I number,
                                VARIATION_O out number) 
     RETURN number;
function VALIDATE_MOVE_ROOK(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number) 
    RETURN number;
function VALIDATE_MOVE_BISHOP(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number)RETURN number;
function VALIDATE_MOVE_KNIGHT(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number) 
    RETURN number;
function VALIDATE_MOVE_QUEEN(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number) 
    RETURN number;
    function VALIDATE_MOVE_KING(MATCH_ID_I MATCH.MATCH_ID%type,
                                X1 number,                           
                                Y1 number,
                                X2 number, 
                                Y2 number) 
    RETURN number;
function PRINT_BOARD(MATCH_ID_I MATCH.MATCH_ID%type)RETURN varchar;
function PIECE_TYPE_TO_SYMBOL(TYPE_I SQUARE.PIECE_TYPE%type,COLOR_I SQUARE.PIECE_COLOR%type)RETURN char;
procedure CREATE_NEW_PLAYER(PLAYER_ID_I PLAYER.PLAYER_ID%type, PLAYER_NAME_I PLAYER.PLAYER_NAME%type, RETURN_CODE_O out number);
procedure DELETE_PLAYER(PLAYER_ID_I PLAYER.PLAYER_ID%type, RETURN_CODE_O out number);
procedure CREATE_NEW_MATCH(WHITE_PLAYER_ID_I PLAYER.PLAYER_ID%type,BLACK_PLAYER_ID_I PLAYER.PLAYER_ID%type, RETURN_CODE_O out number);
procedure POPULATE_BOARD(MATCH_ID_I MATCH.MATCH_ID%type, RETURN_CODE_O out number);
procedure CLEAR_BOARD(MATCH_ID_I MATCH.MATCH_ID%type, RETURN_CODE_O out number);
procedure RESET_BOARD(MATCH_ID_I MATCH.MATCH_ID%type, RETURN_CODE_O out number);
procedure MOVE( MATCH_ID_I MATCH.MATCH_ID%type,        
                    FILE1_I char,  
                    RANK1_I char,  
                    FILE2_I char,  
                    RANK2_I char, 
                    RETURN_CODE_O out number, MSG out varchar);
end Test;
/
