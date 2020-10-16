// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Runtime.Serialization;

namespace Pulumi.PlantProvider.Tree.V1
{
    /// <summary>
    /// types of rubber trees
    /// </summary>
    public readonly struct RubberTreeVariety : IEquatable<RubberTreeVariety>
    {
        private readonly string _value;

        private RubberTreeVariety(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// A burgundy rubber tree.
        /// </summary>
        public static RubberTreeVariety Burgundy { get; } = new RubberTreeVariety("Burgundy");
        /// <summary>
        /// A ruby rubber tree.
        /// </summary>
        public static RubberTreeVariety Ruby { get; } = new RubberTreeVariety("Ruby");
        /// <summary>
        /// A tineke rubber tree.
        /// </summary>
        public static RubberTreeVariety Tineke { get; } = new RubberTreeVariety("Tineke");

        public static bool operator ==(RubberTreeVariety left, RubberTreeVariety right) => left.Equals(right);
        public static bool operator !=(RubberTreeVariety left, RubberTreeVariety right) => !left.Equals(right);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object obj) => obj is RubberTreeVariety other && Equals(other);
        public bool Equals(RubberTreeVariety other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
