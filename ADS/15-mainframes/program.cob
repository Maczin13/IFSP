       IDENTIFICATION DIVISION.
       PROGRAM-ID. BATCH-POSTING.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INPUT-FILE ASSIGN TO 'INPUT.DAT'
               ORGANIZATION IS SEQUENTIAL.
           SELECT ACCEPT-FILE ASSIGN TO 'ACCEPT.DAT'
               ORGANIZATION IS SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD INPUT-FILE.
       01 INPUT-RECORD.
           05 IN-ID      PIC X(06).
           05 IN-DATE    PIC 9(08).
           05 IN-AMOUNT  PIC 9(12).
           05 IN-STATUS  PIC X(10).
       FD ACCEPT-FILE.
       01 ACCEPT-RECORD PIC X(36).
       WORKING-STORAGE SECTION.
       01 WS-EOF        PIC X VALUE 'N'.
       01 WS-READ       PIC 9(09) VALUE 0.
       01 WS-ACCEPTED   PIC 9(09) VALUE 0.
       01 WS-REJECTED   PIC 9(09) VALUE 0.
       PROCEDURE DIVISION.
           OPEN INPUT INPUT-FILE OUTPUT ACCEPT-FILE
           PERFORM UNTIL WS-EOF = 'Y'
               READ INPUT-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END
                       ADD 1 TO WS-READ
                       IF IN-AMOUNT > 0
                           WRITE ACCEPT-RECORD FROM INPUT-RECORD
                           ADD 1 TO WS-ACCEPTED
                       ELSE
                           ADD 1 TO WS-REJECTED
                       END-IF
               END-READ
           END-PERFORM
           CLOSE INPUT-FILE ACCEPT-FILE
           DISPLAY 'READ=' WS-READ ' ACCEPTED=' WS-ACCEPTED
                   ' REJECTED=' WS-REJECTED
           GOBACK.
