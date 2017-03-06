import mysql.connector;

class Mysqlib:
    _config     = None;
    _connection = None;
    _cursor     = None;
    _error      = '';

    def __init__(self, config):
        try:
            self._config = config;
            self._connection = mysql.connector.connect(
                host = self._config['host'] if 'host' in self._config.keys() else self._config['hostname'],
                port = self._config['port'],
                user = self._config['user'] if 'user' in self._config.keys() else self._config['username'],
                password = self._config['passwd'] if 'passwd' in self._config.keys() else self._config['password'],
                database = self._config['db'] if 'db' in self._config.keys() else self._config['database'],
                charset = self._config['charset'],
                connection_timeout = self._config['timeout'] if 'timeout' in self._config.keys() else self._config['connection_timeout']
            )
            self._cursor = self._connection.cursor(buffered=True);
        except mysql.connector.DatabaseError as e:
            self._error = e
            raise Exception(e)

    def query(self, sql):
        try:
            self._cursor.execute(sql);
            self._connection.commit();
        except mysql.connector.DatabaseError as e:
            self._connection.rollback();
            self._error = e.msg;
            raise Exception(e)

    def fetchAll(self, sql, assoc=True):
        self.query(sql);
        if(assoc):
            columns = self._cursor.description;
            return [{columns[index][0]:column for index, column in enumerate(value)} for value in self._cursor.fetchall()];
        else:
            return self._cursor.fetchall();

    def fetchOne(self, sql, assoc=True):
        self.query(sql);
        if(assoc):
            columns = self._cursor.description;
            return {columns[index][0]:column for index, column in enumerate(self._cursor.fetchone())};
        else:
            return self._cursor.fetchone();

    def rowCount(self, sql):
        self.query(sql);
        return self._cursor.rowcount;

    def getInsertId(self):
        return self._cursor.lastrowid;

    def getConfig(self):
        return self._config;

    def getConnection(self):
        return self._connection;

    def getCursor(self):
        return self._cursor;

    def getError(self):
        return self._error;