using System;

namespace AoC2020
{
    public class AoCBase
    {
        private int _debugLevel;
        /// <summary>
        /// A base class for the helper classes in this project.
        /// </summary>
        /// <param name="debugLevel">Debug level at which the object should operate. </param>
        public AoCBase(int debugLevel)
        {
            _debugLevel = debugLevel;
        }

        /// <summary>
        /// A shared logging system.
        /// </summary>
        /// <param name="output">The object to be logged.</param>
        /// <param name="level">The level at which to log it. If higher than this class's
        ///     debug level, the message will not be written.</param>
        public void DebugLog(object output, int level = 1) {
            if (_debugLevel >= level) {
                Console.WriteLine(output);
            }
        }
    }
}
