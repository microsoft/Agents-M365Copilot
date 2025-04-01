﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ---------------

namespace Microsoft.Agents.M365Copilot.Core.Helpers
{
    using System;
    using System.Diagnostics;
    using System.IO;

    /// <summary>
    /// Helper stream class to represent a slice of a larger stream to save memory when dealing with large streams
    /// and remove the extra copy operations
    /// This class is inspired from System.IO.Compression in dot net core. Reference implementation can be found here
    /// https://github.com/dotnet/corefx/blob/d59f6e5a1bdabdd05317fd727efb59345e328b80/src/System.IO.Compression/src/System/IO/Compression/ZipCustomStreams.cs#L147
    /// </summary>
    internal class ReadOnlySubStream(Stream superStream, long startPosition, long maxLength) : Stream
    {
        private readonly long _startInSuperStream = startPosition;
        private long _positionInSuperStream = startPosition;
        private readonly long _endInSuperStream = startPosition + maxLength;
        private readonly Stream _superStream = superStream;
        private bool _canRead = true;
        private bool _canSeek = true;
        private bool _isDisposed = false;

        public override long Length
        {
            get
            {
                ThrowIfDisposed();

                return _endInSuperStream - _startInSuperStream;
            }
        }

        public override long Position
        {
            get
            {
                ThrowIfDisposed();

                return _positionInSuperStream - _startInSuperStream;
            }
            set
            {
                ThrowIfDisposed();

                if (!CanSeek)
                    throw new NotSupportedException("seek not support");

                if (value > int.MaxValue || value < 0 || value > Length)
                    throw new ArgumentOutOfRangeException("value is out of range");

                // update the position in base stream and seek to that position
                _positionInSuperStream = value + _startInSuperStream;
                _superStream.Seek(_positionInSuperStream, SeekOrigin.Begin);
            }
        }

        public override bool CanRead => _superStream.CanRead && _canRead;

        public override bool CanSeek => _superStream.CanSeek && _canSeek;

        public override bool CanWrite => false;

        private void ThrowIfDisposed()
        {
            if (_isDisposed)
                throw new ObjectDisposedException(GetType().ToString(), nameof(this._superStream));
        }

        private void ThrowIfCantRead()
        {
            if (!CanRead)
                throw new NotSupportedException("read not support");
        }

        public override int Read(byte[] buffer, int offset, int count)
        {
            // parameter validation sent to _superStream.Read
            int origCount = count;

            ThrowIfDisposed();
            ThrowIfCantRead();

            if (_superStream.Position != _positionInSuperStream)
                _superStream.Seek(_positionInSuperStream, SeekOrigin.Begin);
            if (_positionInSuperStream + count > _endInSuperStream)
                count = (int)(_endInSuperStream - _positionInSuperStream);

            Debug.Assert(count >= 0);
            Debug.Assert(count <= origCount);

            int ret = _superStream.Read(buffer, offset, count);

            _positionInSuperStream += ret;
            return ret;
        }

        public override long Seek(long offset, SeekOrigin origin)
        {
            ThrowIfDisposed();
            switch (origin)
            {
                case SeekOrigin.Begin:
                    Position = offset;
                    break;
                case SeekOrigin.Current:
                    Position += offset;
                    break;
                case SeekOrigin.End:
                    Position = Length - offset;
                    break;
            }

            return Position;
        }

        public override void SetLength(long value)
        {
            ThrowIfDisposed();
            throw new NotSupportedException("write not support");
        }

        public override void Write(byte[] buffer, int offset, int count)
        {
            ThrowIfDisposed();
            throw new NotSupportedException("write not support");
        }

        public override void Flush()
        {
            ThrowIfDisposed();
            throw new NotSupportedException("write not support");
        }

        // Close the stream for reading.  Note that this does NOT close the superStream (since
        // the subStream is just 'a chunk' of the super-stream
        protected override void Dispose(bool disposing)
        {
            if (disposing && !_isDisposed)
            {
                _canRead = false;
                _isDisposed = true;
            }
            base.Dispose(disposing);
        }
    }
}
